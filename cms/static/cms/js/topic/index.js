$.extend( true, $.fn.dataTable.defaults, {
    "searching": false,
    "autoWidth": false,
    "columnDefs": [
        { width: '5%', targets: 0 },
        { width: '20%', targets: 1 },
        { width: '45%', targets: 2 },
        { width: '15%', targets: 3 },
        { width: '15%', targets: 4 },
    ]
} );

$(document).ready(function() {
    $('#items').DataTable();

    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-topic').append(en.cms.breadcrumb.topic);

    // Table headers
    $('#header-name').append(en.cms.header.name);
    $('#header-description').append(en.cms.header.description);
    $('#header-order').append(en.cms.header.order);
    $('#header-subject').append(en.cms.header.subject);

    $('#main-title').append(en.cms.breadcrumb.topic);

    $('#add').append(en.cms.action.add_topic);
} );
