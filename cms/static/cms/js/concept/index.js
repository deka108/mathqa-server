$(document).ready(function() {
    $('#items').DataTable();
    // Table headers
    $('#header-name').append(en.cms.header.name);
    $('#header-description').append(en.cms.header.description);
    $('#header-topic').append(en.cms.header.topic);

    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-concept').append(en.cms.breadcrumb.concept);

    $('#main-title').append(en.cms.breadcrumb.concept);

    $('#add').append(en.cms.action.add_concept);
} );
