resource "aws_cloudwatch_log_group" "option_quote_history" {
  name              = "/aws/lambda/${aws_lambda_function.option_quote_history.function_name}"
  retention_in_days = 7
}
