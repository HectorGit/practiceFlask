$(document).ready(function () {   

    console.log('index JS, document ready , ABOUT javascript connected')

    /* POSSIBLE EXPERIMENT - ADD CLASS CURRENT TO THE ABOUT A HREF */


    current_tab_hyperlink = $('#about_nav_link')

    console.log(current_tab_hyperlink)

    /* THIS SHOULD UNDERLINE OUR CURRENT LINK */
    //current_tab_hyperlink.classList.add("current")
    current_tab_hyperlink.addClass('current')

});