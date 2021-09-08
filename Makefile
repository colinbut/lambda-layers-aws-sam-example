STACK_NAME 	?= lambda-layers-aws-sam-example --region eu-west-1
REGION 		?= eu-west-1

build:
	sam build

deploy:
	sam deploy --no-confirm-changeset

destroy:
	sam delete --no-prompts --stack-name $(STACK_NAME) --region $(REGION)