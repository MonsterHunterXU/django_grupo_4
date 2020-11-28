var CACHE_NAME = 'my-site-cache';
var urlsToCache = [
    '/',
    '/static/css/estolo.css',
    '/static/css/login.css',
    '/Galeria',
    '/Quienes_Somos',
    '/static/dist/css/lightbox.min.css'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
    .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(

    fetch(event.request)
    .then((result)=>{
      return caches.open(CACHE_NAME)
      .then(function(c) {
        c.put(event.request.url, result.clone())
        return result;
      })
      
    })
    .catch(function(e){
        return caches.match(event.request)
    })
 
  );
});

/////////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');



// Your web app's Firebase configuration
    var firebaseConfig = {
        apiKey: "AIzaSyDYdyWrPIrK2pRxgGpHfpv8WtXpkSzImVw",
        authDomain: "djangogrupo4002d.firebaseapp.com",
        databaseURL: "https://djangogrupo4002d.firebaseio.com",
        projectId: "djangogrupo4002d",
        storageBucket: "djangogrupo4002d.appspot.com",
        messagingSenderId: "503019729313",
        appId: "1:503019729313:web:40beaea3e2c9be308ddbe0"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
///////////////////////////////////////
    let messaging = firebase.messaging();

//Generar modelo de notificaciones push por Firebase
    messaging.setBackgroundMessageHandler(function(payload) {
      let titulo = 'Nuevo Insumo Agregado'
      let opciones = {
          body: 'Se ha agregado un nuevo insumo al sistema',
          icon: '/static/img/iconos-pack1/png/008-car service.png'
      }
    self.registration.showNotification(titulo, opciones)
  })
  ///////////////////////////////////////////////////////

