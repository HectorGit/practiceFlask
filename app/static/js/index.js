// import {tns} from './src/tiny-slider.js';

// var slider;

$(document).ready(function () {   

    console.log('index JS, document ready , javascript connected')

    /* PARTNERSHIP SLIDER  */

    var partnerships_slider_left = tns({
        container:'#partnerships_slider_left',
        items: 1,
        controls: false,
        nav: false 
    })

    var partnerships_slider_right = tns({
        container:'#partnerships_slider_right',
        items: 1,
        controls: false,
        nav: false 
    })

    $('#partnerships_next_button').click(function () {
        console.log("partnership next button");
        partnerships_slider_left.goTo('next');
        partnerships_slider_right.goTo('next');
    })
    
    $('#partnerships_prev_button').click (function () {
        console.log("partnership prev button");
        partnerships_slider_left.goTo('prev');
        partnerships_slider_right.goTo('prev');
    })

    /* TEAM SLIDER  */

    var team_slider_left = tns({
        container:'#team_slider_left',
        items: 1,
        controls: false,
        nav: false 
    })

    var team_slider_right = tns({
        container:'#team_slider_right',
        items: 1,
        controls: false,
        nav: false 
    })

    $('#team_next_button').click(function () {
        console.log("team next button");
        team_slider_left.goTo('next');
        team_slider_right.goTo('next');
    })
    
    $('#team_prev_button').click (function () {
        console.log("team prev button");
        team_slider_left.goTo('prev');
        team_slider_right.goTo('prev');
    })

});




$("#mc-embedded-subscribe-form").on("submit", function (event) {  
    console.log('clicked subscribe button') 
    event.preventDefault();
    // var form = document.getElementById('mc-embedded-subscribe-form')
    // $.ajax({
    //     type: 'POST',
    //     url: "/add_newsletter",
    //     data: {
    //         "email_address": form.EMAIL.value
    //     },
    //     success: function (response) {
    //         return console.log("success!")
    //     },
    //     error: function (error) {
    //         console.log("###################")
    //         return console.log(error)
    //     }
    // })
})