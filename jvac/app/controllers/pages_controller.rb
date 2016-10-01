class PagesController < ApplicationController
  def home
    @title = 'Home'
  end


  def login
    @title = 'LogIn'
  end
end
