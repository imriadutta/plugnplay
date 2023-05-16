let otp_gen, count = 0;

$(document).on('submit', '#post-form', function (e) {
    if (count == 0) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/sendOTP',
            data: {
                email: $('#email').val(),
                password: $('#password').val(),
                cpassword: $('#cpassword').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                console.log(data);
                otp_gen = data
                $(".alert").css("display", "block")
                if (otp_gen == -1) {
                    document.getElementById('otp-msg').innerHTML = 'Already registered email! Try with new one.'
                    count--
                    $('#post-form').trigger('reset')
                }
                else if (otp_gen == -2) {
                    document.getElementById('otp-msg').innerHTML = 'Passwords not matched. Try again!'
                    count--
                    $('#post-form').trigger('reset')
                }
                else {
                    $(".next").attr("disabled", "disabled")
                    document.getElementById('otp-msg').innerHTML = 'Sent an otp to your email.'
                    $("#otp").css("display", "block")
                }
            }
        });
    }
    else if (count == 1) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/confirmOTP',
            data: {
                otp: $('#otp').val(),
                otp_gen: otp_gen,
                fullname: $('#fullname').val(),
                email: $('#email').val(),
                password: $('#password').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
                console.log(data);
                $(".alert").css("display", "block")
                if (data == 1) {
                    $("#otp").attr("disabled", "disabled")
                    document.getElementById('otp-msg').innerHTML = `Email registered successfully! 
                    <a href="/login" style="color: white;">Login here</a>`
                    $('#post-form').trigger('reset')
                    $(".next").removeAttr("disabled")
                    count = 0
                    $("#otp").removeAttr("disabled")
                    $("#otp").css("display", "none")
                }
                else {
                    document.getElementById('otp-msg').innerHTML = 'Wrong OTP!'
                    count--
                    $('#post-form').trigger('reset')
                }
            }
        })
    }
    count++
})