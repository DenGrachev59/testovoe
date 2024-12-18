from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_html_content(self):
        return """
            <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Bootstrap demo</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                  </head>
                  <body>
                    <div class="container">
                  <!-- Content here -->
                        <div class="row mt-5">
                            <div class="col-6">
                                <div class="card bg-primary">
                                    <div class="card-body text-white">
                                        <h3 class="card-title"> Contact information </h3>
                                        <div class="row">
                                            <div class="col-6">Москва</div>
                                            <div class="col-6">+7 777 777 777</div>
                                            <div class="col-6">Санкт-Петербург</div>
                                            <div class="col-6">+7 888 888 888</div>
                                        </div>
                                    </div>
                
                                </div>
                            </div>
                            <div class="col-6">
                
                                <div class="card">
                                    <div class="card-body">
                                        <h3 class="card-title"> Форма заявки </h3>
                                        <form>
                                          <div class="mb-3">
                <!--                            <label for="exampleInputEmail1" class="form-label">Email address</label>-->
                                            <input name="name" type="text" class="form-control" id="exampleInputEmail1"  placeholder="Введите имя">
                <!--                            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>-->
                                          </div>
                                          <div class="mb-3">
                <!--                            <label for="exampleInputPassword1" class="form-label">Password</label>-->
                                            <input name="email" type="email" class="form-control" id="exampleInputPassword1" placeholder="Введите E-mail:">
                                          </div>
                                          <div class="mb-3">
                                              <textarea name = "message" class="form-control" id="exampleFormControlTextarea1" placeholder="сообщение" rows="3"></textarea>
                                          </div>
                
                                          <button type="submit" class="btn btn-primary form-control">Отправить</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                  </body>
                </html>
        """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
