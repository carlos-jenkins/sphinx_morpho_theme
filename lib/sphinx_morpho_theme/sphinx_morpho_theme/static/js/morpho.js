(function($){
  $(function(){

    // Enable mobile navigation sidebar
    $('.button-collapse').sideNav({'edge': 'left'});

    $('.search-input').focus( function(){
        $('.search-wrapper').addClass('search-active');
    });

    $('.search-input').blur( function(){
        $('.search-wrapper').removeClass('search-active');
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space
