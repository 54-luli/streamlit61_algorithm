import streamlit as st
import datetime
from algorithms import bubble_sort, select_sort, insert_sort, shell_sort, quick_sort, merge_sort, heap_sort, \
    bucket_sort, radix_sort, counting_sort


# 程序入口
def main():
    # 应用页面设置（显示在网站标签）
    st.set_page_config(page_title="路明非的算法笔记", page_icon=":rainbow:", layout="wide", initial_sidebar_state="auto")
    # 加载成功动画
    st.balloons()

    a11, a12 = st.columns([3, 7])
    with a11:
        a11.success('## ' + datetime.datetime.now().strftime("%Y-%m-%d"))
    with a12:
        a12.info("## 欢迎来到路明非的算法笔记")
    # 分割线
    st.markdown('''---''')

    st.markdown("""#### 参考1：[算法通关手册（LeetCode）](https://algo.itcharge.cn/01.Array/02.Array-Sort)""")
    st.markdown("""#### 参考2：[python实例](https://www.runoob.com/python3/python3-examples.html)""")
    st.markdown('''---''')

    b11, b12, _ = st.columns([1, 1, 1])
    with b11:
        algo_selectbox = st.selectbox(label="", options=["请选择一个算法", "1-冒泡排序", "2-选择排序", "3-插入排序", "4-希尔排序",
                                                         "5-快速排序", "6-归并排序", "7-堆排序", "8-桶排序", "9-基数排序", "10-计数排序"])
    st.markdown('''---''')

    @st.cache
    def data():
        if algo_selectbox == "请选择一个算法":
            return None
        elif algo_selectbox == "1-冒泡排序":
            return bubble_sort
        elif algo_selectbox == "2-选择排序":
            return insert_sort
        elif algo_selectbox == "3-插入排序":
            return select_sort
        elif algo_selectbox == "4-希尔排序":
            return shell_sort
        elif algo_selectbox == "5-快速排序":
            return quick_sort
        elif algo_selectbox == "6-归并排序":
            return merge_sort
        elif algo_selectbox == "7-堆排序":
            return heap_sort
        elif algo_selectbox == "8-桶排序":
            return bucket_sort
        elif algo_selectbox == "9-基数排序":
            return radix_sort
        elif algo_selectbox == "10-计数排序":
            return counting_sort

    if data():
        st.write(data().compare)
        st.write(data().compares)
        c11, c12 = st.columns([4, 1])
        with c11:
            st.code(data().code, language="python")
        with c12:
            text = st.text_input(label="请输入您的数组（例：54,26,17,31,20,13）：",
                                 value="54,26,17,31,20,13")
            if st.button("运行") and text:
                res = list(map(int, text.strip().split(',')))
                st.write("算法的运行结果是：", data().sort_array(res))

    st.image('sort.png')
    st.image('a11.png')


# 运行：streamlit run app_myalgo.py
if __name__ == '__main__':
    main()
