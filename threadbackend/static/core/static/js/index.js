var colors = ['#96B093', '#ECC7D0', '#FFCA8C', '#5B8EE4', '#E2C5E7', '#BDC49E', '#E38871', '#EEBB3E'];

var i;
var imgs = $('#boxes > .row > div > a > img');
for (i = 0; i < imgs.length; i ++) {
    var selected = imgs.get(i);
    $(selected).css('box-shadow', '8px 8px ' + colors[i % colors.length]);
}
