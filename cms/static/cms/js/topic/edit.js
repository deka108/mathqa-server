$(document).ready(function() {
    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-topic').append(en.cms.breadcrumb.topic);
    $('#breadcrumb-edit').append(en.cms.action.edit);

    $('#main-title').append(en.cms.action.edit + " " + en.cms.breadcrumb.topic);
} );
