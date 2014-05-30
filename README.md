tmvc
----
tmvc 是一个基于 tornado 的 python web 框架，在 tornado 的基础上实现 MVC 架构。借鉴ASP.NET MVC，没有花费多少功夫来写代码，重要的是思路。

####Controller
控制器放到 `/controllers` 文件夹下，以 `xxxController` 命名，框架在启动时会自动加载以此命名的控制器，并生成路由。

####View
`/views` 文件夹用来存放视图文件，比如 `HomeController` 对应的视图路径为 `/views/home`，在 `HomeController` 中调用 `self.render_view('index.html')` 对应的文件为 `/views/home/index.html`。

####Model
`/models` 文件夹用来存放数据持久层对象或结构体。

####Route
`routes.py` 为路由文件，这里可以加入自定义路由，默认情况下首页是 `HomeController.index`。
路由是根据 `/controllers` 里的文件自动生成的，比如这个框架跑起来会自动生成这些：

|url         |controller.action     |
|------------|----------------------|
|/home       |HomeController.index  |
|/home/index |HomeController.index  |
|/home/about |HomeController.about  |
|/user       |UserController.index  |
|/user/index |UserController.index  |
