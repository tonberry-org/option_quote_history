resource "aws_lambda_function" "option_quote_history" {
  function_name    = "option_quote_history"
  role             = aws_iam_role.option_quote_history_lambda.arn
  filename         = "../dist/option_quote_history.zip"
  source_code_hash = filebase64sha256("../dist/option_quote_history.zip")
  handler          = "newrelic_lambda_wrapper.handler"
  runtime          = "python3.9"
  publish          = true
  timeout          = 60

  environment {
    variables = {
      # For the instrumentation handler to invoke your real handler, we need this value
      NEW_RELIC_LAMBDA_HANDLER = "option_quote_history.lambda_function.lambda_handler"
      NEW_RELIC_ACCOUNT_ID     = data.aws_ssm_parameter.newrelic_account_id.value
      # Enable NR Lambda extension if the telemetry data are ingested via lambda extension
      NEW_RELIC_LAMBDA_EXTENSION_ENABLED = true
      # Enable Distributed tracing for in-depth monitoring of transactions in lambda (Optional)
      NEW_RELIC_DISTRIBUTED_TRACING_ENABLED = true
      CODE : data.aws_ssm_parameter.code.value
      CLIENT_ID : data.aws_ssm_parameter.client_id.value
      STRIKE_COUNT : 75
      EXPIRATION_RANGE : 90,
      DDB_QUOTE_TABLE : aws_dynamodb_table.option_quote_history.name,
      DDB_UNDERLYING_TABLE : aws_dynamodb_table.option_history_underlying_quotes.name
    }
  }
  layers = ["arn:aws:lambda:us-west-2:451483290750:layer:NewRelicPython39:36"]
}
data "aws_lambda_function" "new_relic" {
  function_name = "newrelic-log-ingestion"
}
resource "aws_cloudwatch_log_subscription_filter" "option_quote_history" {
  name            = "logdna-logfilter"
  log_group_name  = aws_cloudwatch_log_group.option_quote_history.name
  filter_pattern  = ""
  destination_arn = data.aws_lambda_function.new_relic.arn
}

