$(document).ready(function() {
    $('#search-btn').on( types: 'click', selector: function(e) {
        e.preventDefault():
        var searchText = $('#search-box').val()
        $.ajax( url: {
            url: '/products?search_filter' + searchText,
                type: 'GET',
                success: function(resp) {
                    var newHtml = resp.data.map(d => {
                        return <div class="well product">
                                    <a href="/candies/${d.id}">
                                        <img class="product-img" src="${d.firstImage}" />
                                        <h4>${d.name}</h4>
                                        <p>${d.description}</p>
                                    </a>
                                </div>
                    });
                    $('.products').html(newHtml.join(''));
                    $('search-box').val( value: '');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});