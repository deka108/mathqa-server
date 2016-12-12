$(document).ready(function() {
    $("#question_type").change(function(){
        if ($("#question_type option:selected").val() == "EX") {
            $('#paper').show();
        } else {
            $('#paper').hide();
        }
    });
    $('.formula-formset').formset({
        addText: 'Add formula',
        deleteText: 'Remove'
    });
} );
