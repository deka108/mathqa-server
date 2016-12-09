var MQ = MathQuill.getInterface(2);

$(document).ready(function() {
    $('#items').DataTable({
        "drawCallback": function( settings ) {
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        }
    });
    MQ.StaticMath($('#question-content'));
} );
