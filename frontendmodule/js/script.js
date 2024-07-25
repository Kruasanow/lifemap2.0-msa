function ShowPdata() {
    var p = document.getElementById('p-data').innerHTML = 'index-p-data';
    return p
}
// ShowPdata()

$(document).ready(function() {
    $('#send-data').click(function() {
        var data_to_send = {
            'message':'sex',
            'data':'page'
        };

        $.ajax({
            url: 'http://localhost:5050/api/login',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data_to_send),
            success: function(response) {
                alert(stringify(response))
                $('#data').text(JSON,stringify(response));
            },
            error : function() {
                $('#data').text('error with data');
            }
        });
    });
});