from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Issue, Email

from random import shuffle

import os

def index(request, email=None):

    email = request.GET.get('email')
    if email:
        subscribe = Email(email=email)
        subscribe.save()

    three_latest_articles = Article.objects.order_by('date')[0:3]
    latest_issue = Issue.objects.order_by('date').last()
    articles = Article.objects.all()

    context = {
        "three_latest_articles": three_latest_articles,
        "latest_issue": latest_issue,
        "articles": articles,
        "email": email,
    }
    return render(request, 'sections/index.html', context)
    # return HttpResponse("lol")



def about(request, email=None):

    email = request.GET.get('email')
    if email:
        subscribe = Email(email=email)
        subscribe.save()

    return render(request, 'sections/about.html', {"email": email,})



def issues(request, issue_term=None, email=None):

    email = request.GET.get('email')
    if email:
        subscribe = Email(email=email)
        subscribe.save()

    issue_term = request.GET.get('issue_term')
    if issue_term:
        print(issue_term)
        issue_focus = Issue.objects.all().filter(term=issue_term)
    else:
        issue_focus = Issue.objects.all().filter(term=Issue.objects.all().last().term)

    latest_4_issue = Issue.objects.order_by('date')[::-1][0:4]
    all_issues = Issue.objects.order_by('date')[::-1]

    issues_split_by_fours = []

    grouped_issues = []
    first = True
    for i in range(0, len(all_issues)):
        if i % 4 == 0 and not first:
            issues_split_by_fours.append(grouped_issues)
            grouped_issues = []
        elif first:
            first  = False
        grouped_issues.append(all_issues[i])
    issues_split_by_fours.append(grouped_issues)


    context = {
        "latest_4_issue": latest_4_issue,
        "all_issues": all_issues,
        "issue_focus": issue_focus,
        "issues_split_by_fours": issues_split_by_fours[1:],
        "email": email,
    }
    return render(request, 'sections/issues.html', context)

def articles(request, tag=None, article_id=None, email=None):

    email = request.GET.get('email')
    if email:
        subscribe = Email(email=email)
        subscribe.save()

    article_id = request.GET.get("article_id")
    if article_id:
        id = request.GET.get('article_id')

        if id:
            article = Article.objects.all().filter(id=article_id)
            if article != []:
                article = article[0]
                articles = Article.objects.all().filter(tag=article.tag).order_by('?')

                context = {
                    "article": article,
                    "articles": articles,
                    "email": email,

                }

            else:
                return render(request, 'sections/404.html', {})
        else:
            return render(request, 'sections/404.html', {})

        return render(request, 'sections/article.html', context)
    else:
        tag = request.GET.get('tag')
        if tag:
            if tag =="fashion":
                articles = Article.objects.all().filter(tag="fashion")

            elif tag == "art":
                articles = Article.objects.all().filter(tag="art")
            elif tag == "lifestyle":
                articles = Article.objects.all().filter(tag="lifestyle")
            else:
                return render(request, 'sections/404.html', {})
        else:
            tag = "fashion"
            articles = Article.objects.all().filter(tag="fashion")

        if len(articles) >= 3:
            first_few_articles = articles[0:3]
            rest_of_articles = articles[3:][::-1]

            issues_split_by_fours = []

            grouped_issues = []
            first = True

            for i in range(0, len(rest_of_articles)):
                if i % 4 == 0 and not first:
                    issues_split_by_fours.append(grouped_issues)
                    grouped_issues = []
                elif first:
                    first  = False
                grouped_issues.append(rest_of_articles[i])
            issues_split_by_fours.append(grouped_issues)

            rest_of_articles = issues_split_by_fours

        elif len(articles) == 2:
            first_few_articles = articles[0:2]
            rest_of_articles = []
        elif len(articles) == 1:
            first_few_articles = articles[0:1]
            rest_of_articles = []
        else:
            first_few_articles = []
            rest_of_articles = []



        latest_6_articles = Article.objects.order_by('date')[::-1][0:6]
        latest_6_articles = [ [latest_6_articles[i], latest_6_articles[i + 1]] for i in range(0, len(latest_6_articles), 2)]

        no_articles = True if len(first_few_articles) == 0 else False

        context = {
            "articles":articles,
            "latest_6_articles": latest_6_articles,
            "tag": tag,
            "first_few_articles": first_few_articles,
            "rest_of_articles": rest_of_articles,
            "no_articles": no_articles,
            "email": email,
        }

        return render(request, 'sections/articles.html', context)
