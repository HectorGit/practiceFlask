$(document).ready(function () {   

    console.log('index JS, document ready , TECHNOLOGY javascript connected')

    current_tab_hyperlink = $('#technology_nav_link')

    console.log(current_tab_hyperlink)

    current_tab_hyperlink.addClass('current')

    var technology_slider = tns({
        container:'#technology_slider',
        items: 1
        ,
        controls: false,
        nav: false 
    })

    
    $('#solar_ink_button').click(function () {
        //technology_slider.goTo(1);
        technology_slider.goTo('first')
    })

    $('#solar_cells_button').click (function () {
        //technology_slider.goTo(2);
        technology_slider.goTo('last')
    })

});
