#!/usr/bin/env python3

from aws_cdk import core

from hello.hello_stack import MyStack


app = core.App()
MyStack(app, "hello-cdk-1", env={'region': 'ap-southeast-2'})
MyStack(app, "hello-cdk-2", env={'region': 'ap-southeast-2'})

app.synth()
