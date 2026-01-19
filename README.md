Mój projekt to solana price tracker
Aplikacja składa się z niezależnego serwera API oraz klientów komunikujących się z nim przez HTTP, co spełnia definicję systemu rozproszonego.
Serwer obsługuje wiele zapytań jednocześnie oraz wykorzystuje mechanizm cache, dzięki czemu wiele żądań może być przetwarzanych współbieżnie.
Celem mojego projektu było zbudowanie trackera dla Kryptowaluty Solana,
tak aby móc co 30 sekund mieć dostęp do ceny w lokalnej przeglądarce.
Na tej podstawie zbudowałem sobie tracker ceny na widgecie na pulpicie, tak aby mieć
do niego łatwy dostęp jako trader.
Dzięki temu nie muszę co chwilę sprawdzać ceny i odświeżać stronę tylko
mam wszystko na widgecie. 
Sposób uruchomienia:
1. Visual Studio
2. Pobrać biblioteki flask, jsonify, requests, time
3. Uruchomić w terminalu program na serwerze
4. Wpisać w przeglądarce adres z terminala(np http://127.0.0.1:5000/price/solana) i odświeżyć

PS: Gdy uruchomimy serwer na komputerze i wpiszemy w przeglądarkę na telefonie 
http://IP_Twojego_komputera:5000/price/solana
to również wyświetli się cena - przydatne do budowania różnych widgetów, trackerów, systemów powiadomień cenowych itd.
