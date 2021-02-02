

$(document).ready(function () {   

    console.log('document ready , javascript connected')

});

// $("#mc-embedded-subscribe-form").on("submit", function (event) {  
//     console.log('clicked subscribe button') 
//     event.preventDefault();
//     var form = document.getElementById('mc-embedded-subscribe-form')
//     $.ajax({
//         type: 'POST',
//         url: "/add_newsletter",
//         data: {
//             "email_address": form.EMAIL.value
//         },
//         success: function (response) {
//             return console.log("success!")
//         },
//         error: function (error) {
//             console.log("###################")
//             return console.log(error)
//         }
//     })
// })