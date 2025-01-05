import React from "react";

interface CourseCardProps {
  courseName: string;
  courseDescription: string;
  courseButton: string;
  image: string;
}

const CourseCard: React.FC<CourseCardProps> = ({
  courseName,
  courseDescription,
  courseButton,
  image,
}) => {
  return (
    <div className="relative mt-12 w-[400px] h-auto bg-primary rounded-lg overflow-hidden hover:shadow-xl transform transition-all hover:scale-[1.02] duration-300">
    {/* Image Container */}
      <div className="aspect-video relative">
        <img
          src={image}
          className="w-full h-full object-cover overflow-hidden"
          alt="Course Thumbnail"
        />
      </div>

      {/* Content Container */}
      <div className="p-4 md:p-6 space-y-4">
        {/* Title */}
        <h2 className="font-workSans text-xl md:text-2xl font-bold text-white text-center">
          {courseName}
        </h2>

        {/* Description */}
        <p className="font-workSans font-light text-white text-base md:text-base text-center leading-relaxed">
          {courseDescription}
        </p>

        {/* Button Container */}
        <div className="pt-4 flex justify-center">
          <button
            className="text-white font-workSans font-bold text-lg md:text-xl 
                           border-2 border-white rounded-full 
                           py-2 px-4 md:py-3 md:px-6
                           transition-all duration-300
                           hover:bg-white hover:text-primary
                           hover:scale-105 active:scale-95"
          >
            {courseButton}
          </button>
        </div>
      </div>
    </div>
  );
};

export default CourseCard;
