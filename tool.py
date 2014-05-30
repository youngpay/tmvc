#coding: utf-8

import sys
import os
import pkgutil
import inspect
import controllers

class Tool(object):

    @staticmethod
    def classes_in_module(module_name):
        if module_name is None:
            raise ValueError("'module_name' can not be None")

        module = __import__("controllers." + module_name, fromlist = [module_name])
        return inspect.getmembers(module, inspect.isclass)

    @staticmethod
    def array_find_by_lambda(list, func):
        return next((index for (index, d) in enumerate(list) if func(d)), -1)
    
    @staticmethod
    def routes_by_controllers():
        controller_path = controllers.__path__
        routes = []
        for importer, name, ispkg in pkgutil.iter_modules(controller_path):
            action_routes = Tool.routes_by_actions(name)
            routes.extend(action_routes)
        return routes

    @staticmethod
    def routes_by_actions(module_name):
        classList = Tool.classes_in_module(module_name)
        baseIndex = Tool.array_find_by_lambda(classList, lambda x:x[0] == "BaseHandler")
        if baseIndex > -1:
            del classList[baseIndex]

        index_action = Tool.array_find_by_lambda(classList, lambda x:x[0] == "index")
        if index_action == -1:
            raise SystemError("controller must have an 'index' action")

        controller_begin = module_name.find(".") + 1
        controller_name = module_name[controller_begin:-10]
        routes = [("/" + controller_name.lower(), classList[index_action][1]), ]
        for (index, item) in enumerate(classList) :
            routes.append(("/" + controller_name.lower() + "/" + item[0].lower(), item[1]))
        return routes