resource "aws_lambda_function" "option_history_quotes" {
  function_name    = "option_history_quotes"
  role             = aws_iam_role.option_history_quotes_lambda.arn
  filename         = "../dist/option_history_quotes.zip"
  source_code_hash = filebase64sha256("../dist/option_history_quotes.zip")
  handler          = "option_history_quotes.lambda_function.lambda_handler"
  runtime          = "python3.9"
  publish          = true
  timeout          = 60

  environment {
    variables = {
      CODE : data.aws_ssm_parameter.code.value
      CLIENT_ID : data.aws_ssm_parameter.client_id.value
      STRIKE_COUNT : 75
      EXPIRATION_RANGE : 90
    }
  }
}
