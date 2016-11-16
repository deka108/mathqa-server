var MQ = MathQuill.getInterface(2);

$(document).ready(function() {
    $('#items').DataTable();
    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-question').append(en.cms.breadcrumb.question);

    $('#main-title').append(en.cms.breadcrumb.question);

    MQ.StaticMath($('#question-content'));
} );
