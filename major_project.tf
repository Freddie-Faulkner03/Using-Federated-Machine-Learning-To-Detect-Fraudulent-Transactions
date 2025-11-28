# declare the cloud provider as AWS
provider "aws" {
  region = "us-east-1"
}

# creates the AWS lambda function using the python language
resource "aws_lambda_function" "model_lambda" {
  function_name = "model-inference"
  handler       = "inference.lambda_handler"
  runtime       = "python3.9"
  role          = "arn:aws:iam::229516761416:role/LabRole"
  filename      = "lambda_inference.zip"
  source_code_hash = filebase64sha256("lambda_inference.zip")
  timeout       = 30
  memory_size   = 512
}

# creates the http trigger
resource "aws_apigatewayv2_api" "http_api" {
  name          = "model-api"
  protocol_type = "HTTP"
}

# creates the lambda permission needed to allow the function to be invoked
resource "aws_lambda_permission" "api_gateway" {
  statement_id  = "AllowInvokeFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.model_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# allows the results of the model to be sent back in a post request
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.http_api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.model_lambda.invoke_arn
  integration_method = "POST"
  payload_format_version = "2.0"
}

# defines the gateway route used by api gateway
resource "aws_apigatewayv2_route" "default_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "POST /predict"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# creates the stage for the api gateway
resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = "$default"
  auto_deploy = true
}

# exposes the api gateway public endpoint url
output "api_endpoint" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}
