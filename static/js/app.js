// if('serviceWorker' in navigator){
//     navigator.serviceWorker.register('/sw.js', {scope: '.'})
//       .then(reg => console.log('service worker registered'))
//       .catch(err => console.log('service worker not registered', err));
//   }
  (function() {
    if('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
                 .then(function(registration) {
                 console.log('Service Worker Registered');
                 return registration;
        })
        .catch(function(err) {
          console.error('Unable to register service worker.', err);
        });
        navigator.serviceWorker.ready.then(function(registration) {
          console.log('Service Worker Ready');
        });
      });
    }
  })();