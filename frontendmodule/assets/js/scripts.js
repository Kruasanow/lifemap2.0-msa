function showAddict() {
    document.getElementById('addInformation').addEventListener('click', function() {
        var fields = document.getElementById('addInformationField');
        fields.style.display = fields.style.display === 'none' ? 'block':'none';
    });
};
showAddict();

function createEvent() {
    document.getElementById('createEvent').addEventListener('click', function() {
        var fields = document.getElementById('eventCreation');
        fields.style.display = fields.style.display === 'none' ? 'block' : 'none';
    });
}
createEvent();