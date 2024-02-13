export const variants = (direction) => {
    return{
    hidden: 
    {y: direction==='up' ? -40: direction === 'down'? 40: 0, 
    opacity: 0,
    x: direction==='left' ? -40: direction === 'right'? 40: 0,
 },
    visible: {
      opacity: 1,
      y: 0,
      x: 0,
      transition: {
        type: "spring",
        duration: 1.8
      }
    }
    }
  }
