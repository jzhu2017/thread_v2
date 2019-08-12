//regular view
if ($(window).width() > 500) {

	//calculate height that we need to scroll past
	$('nav').addClass('pastNav').removeClass('py-4');
	var past = $('nav').outerHeight();
	$('nav').removeClass('pastNav').addClass('py-4');

	var bottom = $('nav').outerHeight() - past;

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
}

//for mobile view
if ($(window).width() <= 500) {

	var height = $('#mobile-logo').outerHeight();
	$('body').css('paddingTop', $('#nav-mobile').height());
	$(window).on('scroll', function() {
		var stop = Math.round($(window).scrollTop());
		if (stop > height) {
			$('#nav-mobile').addClass('nav-up');
		}
		else {
			$('#nav-mobile').removeClass('nav-up');
		}
	});
}
