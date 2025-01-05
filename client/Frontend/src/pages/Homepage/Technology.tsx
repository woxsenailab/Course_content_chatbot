import CourseCard from "../../components/Cards/Card";
import AI from "../../Assests/CourseImages/ai_thumnail.png";
import Finance from "../../Assests/CourseImages/Finance.png";
import Marketing from "../../Assests/CourseImages/marketingthumbnail.png";

const app = () => {
  return (
    <div className="mx-auto w-full">
      <div className="">
        {/* technology */}
        <div className="ml-28 inline-block font-workSans font-bold text-2xl text-white text-center px-12 py-4 bg-primary rounded-3xl">
          Technology
        </div>
        {/* technology_cards */}
        <div className="flex gap-8 justify-center">
            <CourseCard
            courseName="ARTIFICIAL INTELLGIENCE"
            courseDescription="Lorem ipsum dolor ipsum dignissimos illo quod sunt expedita, nostrum sapiente nobis eius, aperiam minus modi nisi dolorum mollitia?"
            courseButton="OPEN NOW"
            image={AI}
            />
            <CourseCard
            courseName="FINANCE"
            courseDescription="Lorem ipsum dolor ipsum dignissimos illo quod sunt expedita, nostrum sapiente nobis eius, aperiam minus modi nisi dolorum mollitia?"
            courseButton="OPEN NOW"
            image={Finance}
            />
            <CourseCard
            courseName="MARKETING"
            courseDescription="Lorem ipsum dolor ipsum dignissimos illo quod sunt expedita, nostrum sapiente nobis eius, aperiam minus modi nisi dolorum mollitia?"
            courseButton="OPEN NOW"
            image={Marketing}
            />
            <CourseCard
            courseName="MARKETING"
            courseDescription="Lorem ipsum dolor ipsum dignissimos illo quod sunt expedita, nostrum sapiente nobis eius, aperiam minus modi nisi dolorum mollitia?"
            courseButton="OPEN NOW"
            image={Marketing}
            />
        </div>
      </div>
    </div>
  );
};

export default app;
