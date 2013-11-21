var csrfitems = document.getElementsByName('csrfmiddlewaretoken');
var csrftoken = '';
if (csrftoken.length > 0) {
    csrftoken = csrfitems[0].value;
}
KindEditor.ready(function(K) {
    K.create('#id_content', {
        // height: '400px',
        uploadJson: '/upload/ke_upload/',
        fileManagerJson: '/upload/ke_man/',
        allowFileManager: true,
        extraFileUploadParams: {
            csrfmiddlewaretoken: csrftoken
        },
    });
});