resource "aws_lambda_function" "option_quote_history" {
  function_name    = "option_quote_history"
  role             = aws_iam_role.option_quote_history_lambda.arn
  filename         = "../dist/option_quote_history.zip"
  source_code_hash = filebase64sha256("../dist/option_quote_history.zip")
  handler          = "option_quote_history.lambda_function.lambda_handler"
  runtime          = "python3.9"
  publish          = true
  timeout          = 60

  environment {
    variables = {
      CODE : data.aws_ssm_parameter.code.value
      CLIENT_ID : data.aws_ssm_parameter.client_id.value
      STRIKE_COUNT : 75
      EXPIRATION_RANGE : 90,
      DDB_QUOTE_TABLE : aws_dynamodb_table.option_quote_history.name,
      DDB_UNDERLYING_TABLE : aws_dynamodb_table.option_history_underlying_quotes.name
    }
  }
}
