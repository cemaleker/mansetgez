$(function () {
    jQuery.getJSON('/data.json')
    .done(function(data) {
        for (key in data) {
            var object = data[key]
            var img = $('<img src="' + object['url'] + '" />')
            $('#contents').append(img)
        }
    })
   .fail (function(){ console.log(arguments) })
})
