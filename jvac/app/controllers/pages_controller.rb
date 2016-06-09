class PagesController < ApplicationController

  def home
  	@title = "Home"
  end

  def features
  	@title = "Features"
  end

  def about
  	@title = "About"
  end

   def contact
    @title = "Contact"
     end

     def login
      @title = "LogIn"
    end

    def signup
      @title = "SignUp"
    end

    def more
    @title = "More"
    end


end
