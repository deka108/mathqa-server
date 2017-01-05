$.extend( true, $.fn.dataTable.defaults, {
    "autoWidth": false,
    "columnDefs": [
        { width: '5%', targets: 0 },
        { width: '25%', targets: 1 },
        { width: '50%', targets: 2 },
        { width: '20%', targets: 2 },
    ]
} );

$(document).ready(function() {
    $('#items').DataTable();

    // Breadcum
    $('#breadcrumb-formula').append(en.cms.breadcrumb.formula);

    // Table headers
    $('#header-id').append(en.cms.header.id);
    $('#header-name').append(en.cms.header.name);
    $('#header-content').append(en.cms.header.description);

    $('#main-title').append(en.cms.breadcrumb.formula);

    $('#add').append(en.cms.action.add_formula);
} );
