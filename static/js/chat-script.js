var initialData = [
    { firstName: "Danny", lastName: "LaRusso", phones: [
        { type: "Mobile", number: "(555) 121-2121" },
        { type: "Home", number: "(555) 123-4567"}]
    },
    { firstName: "Sensei", lastName: "Miyagi", phones: [
        { type: "Mobile", number: "(555) 444-2222" },
        { type: "Home", number: "(555) 999-1212"}]
    }
];

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var ContactsModel = {
    getCookie: function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },
    start: function () {
        $.get('/api/messages/?chat='+window.chatId+'&last=20', function (data) {
            this.addMessagesFromServer(data);
            this.startUpdatingChat();
        }.bind(this));
    },
    updateChat: function () {
        var lastMessage = this.messages()[this.messages().length-1];
        var lastDateTime = lastMessage.timestamp;
        $.get('/api/messages/?chat='+window.chatId+'&last_date_time=' + lastDateTime, function (data) {
            this.addMessagesFromServer(data);
        }.bind(this));
    },
    startUpdatingChat: function () {
        setInterval(this.updateChat.bind(this), 1000);
    },
    messages: ko.observableArray(),
    users: ko.observableArray(),
    textMessage: ko.observable(),
    addMessagesFromServer: function (messagesArray) {
        this.messages(this.messages().concat(messagesArray));
        $('.message-list').scrollTop($('.message-list').height());
    },
    addMessage: function (formElement) {
        var text = this.textMessage();
        var csrftoken = this.getCookie('csrftoken');
        $.post('/api/messages/', {
            text: text,
            chat: window.chatId
        }).done(function (data) {
            
        });
    }
};

ko.applyBindings(ContactsModel);

ContactsModel.start();

$(document).ready(function () {
    $('.message-list').resize(function () {
        console.log('resize')
    });
});