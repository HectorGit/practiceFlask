$(document).ready(function () {   

    console.log('index JS, document ready , APPLICATIONS javascript connected')


    current_tab_hyperlink = $('#applications_nav_link')

    console.log(current_tab_hyperlink)

    current_tab_hyperlink.addClass('current')


    var applications_slider = tns({
        container:'#applications_slider',
        items: 1
        ,
        controls: false,
        nav: false 
    })

    
    $('#pv_blinds_button').click(function () {
        applications_slider.goTo(0)
    })

    $('#pv_tiles_button').click (function () {
        applications_slider.goTo(1)
    })


    $('#pv_windows_button').click (function () {
        applications_slider.goTo(2)
    })

});