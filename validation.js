;(function(){
    $.fn.validatePhone = function(){
        var value = $(this).val();
        return /^1[3|5|8][0-9]\d{8}$/.test(value);
    }

    $.fn.validateCode = function(){
        var value = $(this).val();
        console.log(value);
        return /^\d{4,}$/.test(value);
    }

    $.fn.validateEmail = function(){
        var value = $(this).val();
        console.log($(this).val());
        return /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(value);
    }
})(jQuery);