import mlrun


def hello(context: mlrun.MLClientCtx, name: str = "world"):
    context.logger.info(f"Hello, {name}! This message was written by an MLRun job.")
    context.log_result("greeting", f"Hello, {name}!")
