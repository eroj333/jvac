class SessionsController < ApplicationController
  def new
    @title ='LogIn'
  end

  def create
    @user=User.authenticate(params[:session][:email],params[:session][:password])
    if @user.save
      redirect_to user
    else
      render 'new'
    end

  end

  def destroy

  end

end
