$('input[type="range"]').on("change mousemove", function () {
    var val = ($(this).val() - $(this).attr('min')) / ($(this).attr('max') - $(this).attr('min'));

    $(this).css('background-image',
                '-webkit-gradient(linear, left top, right top, '
                + 'color-stop(' + val + ', #FF9906), '  // Color before the thumb
                + 'color-stop(' + val + ', #FFFFFF)'  // Color after the thumb
                + ')'
                );
    var output = document.getElementById("sliderOutput");
    var actualValue = $(this).val() / 10;
    // Display Output
    output.innerHTML = Math.floor(actualValue) * 10 + '%';
});
