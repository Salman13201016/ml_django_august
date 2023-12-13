$(document).ready(function () {
    url = '/admin/division/show/'
    csrf = $('.csrf').val()
    $.ajax({
        type: "GET",
        url: url,
        // data: data,
        // beforeSend: function (xhr) {
        //     xhr.setRequestHeader('X-CSRFToken', csrf);
        // },
        dataType: 'json',
        success: function (response) {

            $('.division_table').empty()
            for (i = 0; i < response.d.length; i = i + 1) {
                // console.log(response.d[i].id)
                console.log(response.d[i].name)
                j = i + 1

                tr = '<tr><td>' + j + '</td><td>' + response.d[i].name + '</td><td>Action|Delete</td></tr>'

                $('.division_table').append(tr)
            }
        }
    });

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

                $('.division_table').empty()
                for (i = 0; i < response.d.length; i = i + 1) {
                    // console.log(response.d[i].id)
                    console.log(response.d[i].name)
                    j = i + 1

                    tr = '<tr><td>' + j + '</td><td>' + response.d[i].name + '</td><td>Action|Delete</td></tr>'

                    $('.division_table').append(tr)
                }
            }
        });
    });
});