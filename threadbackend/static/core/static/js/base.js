$('nav').addClass('pastNav').removeClass('py-4');
var past = $('nav').outerHeight(true);
$('nav').removeClass('pastNav').addClass('py-4');

var bottom = $('nav').outerHeight(true) - past;

$(window).on('scroll', function() {
    var stop = Math.round($(window).scrollTop());
    if (stop > bottom) {
	document.body.style.paddingTop = (bottom + past) + 'px';
	$('nav').addClass('fixed-top pastNav').removeClass('py-4');
	$('#links').removeClass('justify-content-center').addClass('mr-auto');
	$('#logo').removeClass('justify-content-center');
    }
    else {
	document.body.style.paddingTop = 0;
	$('nav').removeClass('fixed-top pastNav').addClass('py-4');
	$('#links').addClass('justify-content-center').removeClass('mr-auto');
	$('#logo').addClass('justify-content-center');
    }
});
