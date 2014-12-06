function submitStart(formData, jqForm, options) {
    $("#errors").hide();
    $("#done").hide();

    setEnabledDisabled(true);
    $("#sendwrapper").prepend('<p class="alert alert-info" role="alert">Sending your bio, please wait... </p>');
    return true;
}

function submitSuccess(responseText, statusText, xhr, form) {
    json_resp_obj = $.parseJSON(responseText);
    setEnabledDisabled(false);
    $("#errors, #sendwrapper, #done").empty();
    if (json_resp_obj.status == "done_status") {
        $("#done").show();
        $("#done").prepend("<p class='alert alert-success' role='alert'>Data saved done.</p>");
    } else {
        $("#errors").show();
        if (json_resp_obj.errors.indexOf(',') == -1) {
            $("#errors").prepend("<p>Error in field " + json_resp_obj.errors + "</p>");
        } else {
            $("#errors").prepend("<p>Errors in fields " + json_resp_obj.errors + "</p>");
        }
    }
}

function setEnabledDisabled(status) {
    $("#id_other_contacts, #id_first_name, #id_last_name, " +
    "#id_birth_date, #id_biography, #id_email, " +
    "#id_skype, #id_jabber, #id_other_contacts").prop('disabled', status);
}

$(function () {
    $("#errors").hide();
    $("#done").hide();
    $("#id_birth_date").datepicker({dateFormat: 'yy-mm-dd'});
    $("#editform").ajaxForm({
        beforeSubmit: submitStart,
        success: submitSuccess
    });
});