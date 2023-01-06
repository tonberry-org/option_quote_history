
resource "aws_dynamodb_table" "option_history_quotes" {
  name         = "option_history_quotes"
  hash_key     = "symbol"
  range_key    = "timestamp"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "symbol"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }

  tags = {
    Name = "Market Scheduler"
  }
}


resource "aws_dynamodb_table" "option_history_underlying_quotes" {
  name         = "option_history_underlying_quotes"
  hash_key     = "id"
  range_key    = "timestamp"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }

  tags = {
    Name = "Market Scheduler"
  }
}
