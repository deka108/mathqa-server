$(document).ready(function() {
    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-topic').append(en.cms.breadcrumb.topic);
    $('#breadcrumb-create').append(en.cms.action.create);

    $('#main-title').append(en.cms.action.create + " " + en.cms.breadcrumb.topic);
} );
