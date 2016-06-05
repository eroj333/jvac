class PagesController < ApplicationController
  def home
  	@title ="Home"
  end

  def features
  	@title = "Features"
  end

  def about
  	@title ="About"
  end
end
