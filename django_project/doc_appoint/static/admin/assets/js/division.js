$(document).ready(function () {
    $('.sub_division').click(function (event) {
        event.preventDefault();

        div_name = $('.division_input').val()
        alert(div_name);

        data = { 'div_name': div_name }
        url = '/admin/division/insert/'
        csrf = $('.csrf').val()

        $.ajax({
            type: "POST",
            url: url,
            data: data,
            beforeSend: function (xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrf);
            },
            dataType: 'json',
            success: function (response) {
                console.log(response)
            }
        });
    });
});