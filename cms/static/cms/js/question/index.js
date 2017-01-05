var MQ = MathQuill.getInterface(2);

$(document).ready(function() {
    $('#items').DataTable({
        "drawCallback": function( settings ) {
        // MathJax.Hub.Config({
        //    tex2jax: {inlineMath: [["$","$"],["\\(","\\)"]]}
        // });
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        }
    });
    // Breadcum
    $('#breadcrumb-question').append(en.cms.breadcrumb.question);

    $('#main-title').append(en.cms.breadcrumb.question);
    MQ.StaticMath($('#question-content'));

    $('.link-answer-formset').formset({
        addText: 'Add new Part',
        deleteText: 'Remove'
    });
});
