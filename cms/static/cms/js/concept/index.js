$.extend( true, $.fn.dataTable.defaults, {
    "searching": false,
    "autoWidth": false,
    "columnDefs": [
        { width: '5%', targets: 0 },
        { width: '40%', targets: 1 },
        { width: '20%', targets: 2 },
        { width: '20%', targets: 3 },
        { width: '15%', targets: 4 }
    ],
    "order": [[ 0, "asc" ]]
} );

$(document).ready(function() {
    $('#items').DataTable();
    // Table headers
    $('#header-order').append(en.cms.header.order);
    $('#header-name').append(en.cms.header.name);
    $('#header-description').append(en.cms.header.description);
    $('#header-topic').append(en.cms.header.topic);

    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-concept').append(en.cms.breadcrumb.concept);

    $('#main-title').append(en.cms.breadcrumb.concept);

    $('#add').append(en.cms.action.add_concept);
} );
